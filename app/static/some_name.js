console.log('Hello world')

function fcn(a,b) {
    return a + b
}
console.log(fcn(2,3))

function fdn(a){
    return a * 4
}
console.log(fdn(3))

function fn(a,b,c){
    return (a + b + c) / 3
}
console.log(fn(3,3,3))

function bn(){
    return 7
}
console.log(bn())

function fr(a){
    return a % 5
}
console.log(fr(12))

$(document).ready(function (){
    $('#id45').click(function (e) {
        alert("Нажата кнопка id='id45")
    })
    $('.class1').click(function (e) {
        alert("Вы действительно хотите выйти?")
    })
      $('#id1').click(function (e) {
        alert($('#input1').val())
    })
        $('#id2').click(function (e) {
        $.post(
            "ajax_path",
            {
                'a': 'hello'
            },
            function (response) {
                alert(response.message)
            }
        );
    })
});
