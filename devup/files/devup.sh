de() {
    # Prepare file to pass the finalize action
    export DEVUP_FINALIZER_FILE="$(\mktemp /tmp/devup-finalize-XXXXXX)"
    \trap "rm -f '${DEVUP_FINALIZER_FILE}'" EXIT

    # Run devup
    env DEVUP_SHELL=1 \de $@
    return_code=$?


    local finalizers
    finalizers=()
    local fin
    while \read -r fin; do
        finalizers+=("${fin}")
    done < "${DEVUP_FINALIZER_FILE}"

    for fin in ${finalizers[*]}; do
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
    done

    # Restore actual return code
    \return ${return_code}
}