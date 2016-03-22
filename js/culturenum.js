
function update_active_menu(){
    var url = window.location.href;
    url_strip = url.split("/").reverse()[0]
    if (url_strip.length > 0){
        $('.module_menu ul li a').removeClass('active');
    }
    $('.module_menu ul li a').filter(function() {
        return this.href == url;
    }).addClass('active');
};

// ## control of Navigation and sections/subsections toggling ##
function navigation(){
    
    
    
    console.log(" loading navigation ???");
    $(".accordion ul li a").click(function(e){
        console.log("click on ",this)
        e.preventDefault();
        current_node = $(this);
        var selector = current_node.attr('data_sec_id');
        console.log('selector ='+selector+';');
        // when clicking on a section, go automatically to first subsection
        if ($(this).hasClass("section")) {
            //go to 1st subsection if selected section is empty
            console.log('Switching to 1st subsection');
            current_node = current_node.next().find('a.subsection')[0];
            selector = $(current_node).attr('data_sec_id');
            console.log('new selector ='+selector+';');
        }
        // turn selected subsection active, if any
        if ($(current_node).hasClass('subsection')){
            $('a.subsection').removeClass('active');
            $(current_node).addClass('active');
        }
        // toggle selected section or subsection (they all use 'section' tag)
        $('section').hide();
        $('#'+selector).show();
        $(document).scrollTop(0);
        // if an iframe is in selected sec or subsec, rename attribute data-src to src
        var iframes = $('#'+selector).find('iframe');
        console.log("found iframes ?", iframes);
        iframes.each(function(idx){
            if ($(this).data('src')){ // only do it once per iframe
                $(this).prop('src', $(this).data('src')).data('src', false);
                console.log("this src = ", $(this).attr('src'))
                }
        })
    });
    // ## nav stays fixed on top when scroll pos > header height ##
    $(document).scroll(function(){
        var header_height = $('header').outerHeight();
        if (window.scrollY > header_height) {
            $('nav.accordion').attr('style', 'position:fixed;top:0;margin-top:0;');
        }
        else {
            $('nav.accordion').attr('style', '');
        }
    });
    
};
// ## Accordion menu: control folding and unfolding of selected sections (see above for content loading) ##
function accordion(){
    (function ($) {
        console.log(" loading accordion ???");
        // adapt main content height to menu height to avoid overlap with footer
        var nav_height = $('nav.menu').outerHeight();
        $('main.content').attr('style', 'min-height:'+nav_height+'px;')
        // folding/unfolding mechanism
        //$('.accordion > li:eq(0) a').addClass('active').next().slideDown();
        $('.accordion a.section').click(function(j) {
            console.log("accordéon ====", $(this));
            var dropDown = $(this).closest('li').find('p');
            $(this).closest('.accordion').find('p').not(dropDown).slideUp();

            if ($(this).hasClass('active')) {
                $(this).removeClass('active');
            } else {
                $(this).closest('.accordion').find('a.section.active').removeClass('active');
                $(this).addClass('active');
            }
            dropDown.stop(false, true).slideToggle();
            j.preventDefault();
        });
    })(jQuery);
}
// ## Fancybox : used for video texts when clicking on text vignets ##
function load_fancybox(){
    console.log(" loading Fancy box ???");
    $(".fancybox").fancybox({
                    padding : '1em',
                    maxWidth : '70%',
                    maxHeight : '90%',
                    fitToView : false,
                    width : '60%',
                    height : '80%',
                    autoSize : false,
                    closeClick : false,
                    openEffect : 'none',
                    closeEffect : 'none',
                    tpl: {
                        next : '<a title="Next" class="fancybox-nav fancybox-next fancybox-wb-next" href="javascript:;"></a>',
                        prev : '<a title="Previous" class="fancybox-nav fancybox-prev fancybox-wb-prev" href="javascript:;"></a>',
                        closeBtn: '<a title="Close" class="fancybox-item fancybox-close fancybox-wb-close" href="javascript:;"></a>'
                    },
                    helpers : {
                            overlay : {
                                css : {
                                    'background' : 'rgba(255, 255, 255, 0.8)'
                                }
                            }
                    }
                    });
                };

// ## control of main modules navigation : load selected module and toggle tab-like navigation ##
$(function(){
    console.log("module loaded !");
    navigation();
    accordion();
    load_fancybox();
    update_active_menu();
    // load accueil on start
    // $('.module_content').load("accueil.html");
    // $(".module_menu ul li a").click(function(e){
    //     e.preventDefault()
    //     $('.module_menu ul li a').removeClass('active');
    //     $(this).addClass('active');
    //     $('.module_content').load($(this).attr('href'), function(){
    //         console.log("module loaded !");
    //         navigation();
    //         accordion();
    //         load_fancybox();
    //         // triggers click on first subsection
    //         setTimeout(function(){
    //             //first = $(".accordion ul li a")[0]
    //             //first.click();
    //         }, 500)
    //     });
    // });
});