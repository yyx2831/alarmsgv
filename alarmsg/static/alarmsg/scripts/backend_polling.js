/**
 * Created by ZING on 2017/6/6 0006.
 */
// function update(id) {
//     $.getJSON("/alarmsg/data/" + id + "/", function (data) {
//         $.each(data, function () {
//             $("#content").html('<p>' + 'id=' + id + ' ' + this.name + ' is a ' + this.subject + ' teacher.</p>');
//         });
//     });
// }
function timeDown(limit, i) {
    limit--;
    if (i > 4) {
        i = 0;
    }
    if (limit < 0) {
        limit = 3;
        // update(i);
        fetch_rec();
        // console.log("test output 1.");
        i++;
    }
    // $('#time').text(limit + '秒后刷新');
    setTimeout(function () {
        timeDown(limit, i);
    }, 1000)
}
function fetch_rec() {
    $.getJSON("/alarmsg/recent/", function (ret) {
        $("#current_alarm_table").html("");     // 清空内容
        $("#category-danger").html("");
        $("#category-warning").html("");
        $("#category-light").html("");
        $.each(ret.msg_fetch, function (i, item) {
            $("#current_alarm_table").append(
                "<tr>" +
                "<td>" + item.itemname + "</td>" +
                "<td>" + item.arrtime+ "</td>" +
                "<td>" + item.arrloc + "</td>" +
                "<td>" + item.itemvalue + "</td>" +
                "</tr>"
            );
        });
        $("#category-danger").append(
            "<b>" + ret.sum_danger + "</b>"
        );
        $("#category-warning").append(
            "<b>" + ret.sum_warning + "</b>"
        );
        $("#category-light").append(
            "<b>" + ret.sum_light + "</b>"
        );
    });
}
function query_start(loc, rec, cat) {
    // $.getJSON("{% url 'query_start' %}?loc="+loc+"&rec="+rec+"&cat="+cat,function (ret) {
    $.getJSON("/alarmsg/querystart/" + loc + "/" + rec + "/" + cat + "/", function (ret) {
        // console.log('query start.')
        $("#query_alarm_table").html("");
        $.each(ret.result, function (i, item) {
            $("#query_alarm_table").append(
                "<tr>" +
                "<td>" + item.itemname + "</td>" +
                "<td>" + item.arrtime + "</td>" +
                "<td>" + item.arrloc + "</td>" +
                "<td>" + item.itemvalue + "</td>" +
                "</tr>"
            );
        });
    });
}
$(document).ready(function () {
    timeDown(3, 0);
    $('#btn_query').click(function () {
        var loc_id = $('#id_selectLoc').val();
        var rec_id = $('#id_selectRecent').val();
        var cat_id = $('#id_selectCategory').val();
        query_start(loc_id, rec_id, cat_id);

    });
})