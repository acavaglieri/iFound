<template>
	<div></div>
</template>

<script>
export default {
    name: "Toasts",
    
    methods: {
        showToast (responseStatus, responseMessage) {
            if (responseStatus === "success") {
                this.$toast.success(responseMessage, {
                    position: "top-center",
                    closeButton: "button",
                })
            }
            else if (responseStatus === "error") {
                this.$toast.error(responseMessage, {
                    position: "top-center",
                    closeButton: "button",
                })
            }
        }
    }
}
</script>
