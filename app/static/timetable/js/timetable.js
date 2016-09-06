$(document).ready(function () {
    $('#calendar').fullCalendar({
        eventSources: [{
            url: '/timetable/api/get_events',
            type: 'GET',
            error: function () {
                alert('О нет! Что-то пошло не так! Сообщи об этом админу.');
            },
        }],
        color: 'yellow',
        textColor: 'black',
        firstDay: 1,
        height: 600,
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        monthNames: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        monthNamesShort: ['Янв.', 'Фев.', 'Март', 'Апр.', 'Май', 'Июнь', 'Июль', 'Авг.', 'Сент.', 'Окт.', 'Ноя.', 'Дек.'],
        dayNames: ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"],
        dayNamesShort: ["ВС", "ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ"],
        buttonText: {
            prev: "<<",
            next: ">>",
            prevYear: "&nbsp; &lt; &lt; &nbsp;",
            nextYear: "&nbsp;&gt;&gt;&nbsp;",
            today: "Сегодня",
            month: "Месяц",
            week: "Неделя",
            day: "День"
        },
        eventRender: function (event, element) {
            element.context.getElementsByClassName('fc-time')[0].innerHTML = event.start._i.slice(11, 16);
        }
    });
});
