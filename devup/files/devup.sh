# DevUp Bash integration

# Mask the python command `de` with this shell function
# This let us change the current shell (current dir and envvars)
de() {
    # Prepare file to pass the finalize actions
    local finalizer_file
    finalizer_file="$(\mktemp /tmp/devup-finalize-XXXXXX)"

    # Be sure to cleanup this file on termination
    \trap "rm -f '${finalizer_file}'" EXIT

    # Run the python devup `de` command
    env DEVUP_FINALIZER_FILE=$finalizer_file \de $@
    # Save the command return to restore it later
    return_code=$?

    # Perform finalize actions
    # local finalizers
    # finalizers=()
    local fin
    while \read -r fin; do
        # finalizers+=("${fin}")

        [ -n "${DEVUP_DEBUG}" ] && echo "Finalize line: ${fin}"

        case "${fin}" in
            cd:*)
                cd "${fin//cd:/}"
                ;;
            setenv:*)
                export "${fin//setenv:/}"
                ;;
            *)
                ;;
        esac

    done < "${finalizer_file}"

    # for fin in ${finalizers[*]}; do
    #     case "${fin}" in
    #         cd:*)
    #             cd "${fin//cd:/}"
    #             ;;
    #         setenv:*)
    #             export "${fin//setenv:/}"
    #             ;;
    #         *)
    #             ;;
    #     esac
    # done

    # Restore the command return code
    \return ${return_code}
}