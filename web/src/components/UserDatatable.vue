
<template>
    <data-table
        :columns="columns"
        url="http://example.test/example">
    </data-table>
</template>

<script>
    import axios from "axios";
//   npm install axioslet $ = JQuery
// function processClick() {
//             $.ajax({
//               type: "GET",  dataType: 'text',
//               url: '/views/notas',
//               success: function(data){
//                   console.log(data);
//               },
//               error: function( jqXhr, textStatus, errorThrown ){
//                   console.log( errorThrown );
//               },
//             });
//         }
// processClick()

    axios.get("https://127.0.0.1:5000/views/notas")
    .then(response => console.log(response))

export default {
    data() {
        return {
            columns: [
                {
                    label: 'ID',
                    name: 'id',
                    filterable: true,
                },
                {
                    label: 'Name',
                    name: 'name',
                    filterable: true,
                },
                {
                    label: 'Email',
                    name: 'email',
                    filterable: true,
                },
            ]
        }
    },
}
</script>