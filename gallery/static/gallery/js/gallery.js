/*global $:false, document: false, location: false*/


$(function () {

    'use strict';

    var hash = location.hash.slice(1),
        fotorama,
        fotorama_opts = {
            nav: 'thumbs',
            thumbwidth: 70,
            thumbheight: 45,
            width: '100%',
            maxwidth: '100%',
            ratio: 820 / 555,
            fit: 'contain',
            autoplay: false,
            loop: true,
            keyboard: true,
            arrows: true
        },
        fotorama_hash__pattern = /fotorama=img-(\d+)-([\.\-_\w]+)/,
        fotorama_hash__element = fotorama_hash__pattern.exec(hash),
        fotorama_content,
        fotorama_cur_el,
        $fotorama_container = $('.i-popup-content__gallery');

    function show_photo_popup(element) {
        $('.i-popup-content__gallery').show();
        $('.i-popup').css('display', 'table');
        if (fotorama === undefined) {
            fotorama = $('#fotorama_popup').fotorama(fotorama_opts).data('fotorama');
        }
        if (fotorama_content !== undefined && fotorama_content.length > 0) {
            fotorama.load(fotorama_content);
        }
        if (fotorama.autoplay) {
            fotorama.startAutoplay();
        }
        fotorama.show(element);
    }

    $(document).on('click', '.b-list__list-item-image-link', function () {
        var event_obj = $(this),
            url = event_obj.closest('.b-list__list-item').find('.b-list__list-item-link').attr('href'),
            fr_cur_el = event_obj.data('fotorama-id');
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                fotorama_content = data.images;
                show_photo_popup(fr_cur_el);
            }
        });
        return false;
    });

    $(document).on('click', '.b-gallery__item-link', function () {
        var event_obj = $(this),
            fr_cur_el = event_obj.data('fotorama-id'),
            url = event_obj.closest('.b-gallery').data('url');
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                fotorama_content = data.images;
                show_photo_popup(fr_cur_el);
            }
        });
        return false;
    });

    function fotorama_hash__parse(fr_hash) {
        var arr_tmp = fr_hash.split('=');
        if (arr_tmp.length !== 2) {
            return false;
        }
        return arr_tmp[1];
    }

    if (fotorama_hash__element !== null) {
        fotorama_cur_el = fotorama_hash__parse(fotorama_hash__element[0]);
        if (fotorama_cur_el) {
            $('.b-list__list-item-image-link[data-fotorama-id="' + fotorama_cur_el + '"]').trigger('click');
            $('.b-gallery__item-link[data-fotorama-id="' + fotorama_cur_el + '"]').trigger('click');
        }
    }

    $fotorama_container.on('fotorama:showend', '.fotorama', function (e, fotorama) {
        var current = fotorama.activeIndex + 1,
            description = fotorama.activeFrame.description,
            fr_hash = 'fotorama=' + fotorama.activeFrame.id;
        $('.i-popup-content__gallery-count').text(current + ' из ' + fotorama.size);
        $('.i-popup-content__gallery-desc').text(description);
        location.hash = fr_hash;
    });

});
