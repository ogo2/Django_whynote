let slide = document.querySelectorAll('.block_news')
var father = document.querySelector('.slider_news')
let slide_id = document.querySelectorAll('.block_news')
let index = 0
var mass_slide = [0, 0, 0]
$(document).ready(function(){
    $(document).on('click', '.next', function () {
        if (index in mass_slide) {
            // father.removeChild(slide[0])
            console.log(true)
            console.log(index)

            // console.log(slide[0])
            slide[index].style.display = 'none';
            index++
            slide[index].style.display = '';
        }else{
            console.log(false)
            console.log(index)

            // console.log(slide[0])
            slide[index].style.display = '';
            index--

            index++
        }
    });
    $(document).on('click', '.previous', function () {
        slide[index].style.display = 'none';
        index--
        if (index in mass_slide) {

            console.log('index--')

            console.log(index)

            // father.removeChild(slide[0])
            console.log(this)
            // console.log(slide[0])
            slide[index].style.display = '';

        }else{
            console.log(false)

            index++
            console.log('index--')
            // father.removeChild(slide[0])
            console.log(this)
            // console.log(slide[0])
            slide[index].style.display = '';

            console.log(index)
        }
    })
})