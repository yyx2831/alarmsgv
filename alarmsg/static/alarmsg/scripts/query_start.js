/**
 * Created by ZING on 2017/7/2 0002.
 */
// $('#btn_query').on('click', function () {
//     // alert('start query');
//     var loc_id = $('#id_selectLoc').val();
//     var rec_id = $('#id_selectRecent').val();
//     var cat_id = $('#id_selectCategory').val();
//     console.log(loc_id);
// })
//
// $('#btn_query').click(function () {
//     var loc_id = $('#id_selectLoc').val();
//     var rec_id = $('#id_selectRecent').val();
//     var cat_id = $('#id_selectCategory').val();
//     console.log(loc_id);
// });

$(document).ready(function () {
    $('#btn_query').on('click', function () {
        console.log('start query');
        var loc_id = $('#id_selectLoc').val();
        var rec_id = $('#id_selectRecent').val();
        var cat_id = $('#id_selectCategory').val();
        console.log(loc_id);
    });
});

