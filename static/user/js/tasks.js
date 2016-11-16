$(document).ready(function () {
    /*
     Обработка собщений об удачной или неудачной отправке файла с заданием.
     Блоки с сообщениями плавно исчезают спустя 2 секунды.
     */
    $("#messages").fadeTo(2000, 500).slideUp(500, function () {
        $("#messages").alert('close');
    });
    /*
     Раскрытие на клик формы для отправки файла в случае, когда форма скрыта,
     но пользователь хочет отправить другой файл.
     */
    $("#send_another_file").click(function () {
        $("#send_task_form").fadeIn(600).show(100, function() {
            $("#send_another_file").hide();
        });
    })
});