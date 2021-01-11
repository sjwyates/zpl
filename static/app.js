Vue.component("add-modal", {
    template: "add-modal-template"
})

Vue.component("upload-modal", {
    template: "upload-modal-template"
})

new Vue({
    el: '#app',
    data: {
        addModal: false,
        uploadModal: false
    },
    methods: {
        printLabels: function(event) {
            event.preventDefault();
            console.log('print labels')
        },
        addSamplePoint: function(event) {
            event.preventDefault();
            console.log('add sample point')
        }
    }
})