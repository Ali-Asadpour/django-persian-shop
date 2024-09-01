$(".category-slider").slick({
  dots: false,
  infinite: false,
  speed: 300,
  slidesToShow: 6,
  slidesToScroll: 1,
  rtl: true,
  arrows: false,
  responsive: [
    {
      breakpoint: 1920,
      settings: {
        slidesToShow: 6,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 4,
        slidesToScroll: 1,
        infinite: true,
        dots: true,
      },
    },
    {
      breakpoint: 760,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: true,
        dots: true,
      },
    },
    {
      breakpoint: 568,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        infinite: true,
        dots: true,
      },
    },
  ],
});

//brandsSlider
$(".slider-brand-body").slick({
  nextArrow: ".next-arrow-brand",
  prevArrow: ".prev-arrow-brand",
  dots: false,
  slidesToShow: 6,
  slidesToScroll: 1,
  rtl: true,
  arrows: true,
  responsive: [
    {
      breakpoint: 1920,
      settings: {
        slidesToShow: 5,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        dots: false,
        arrows: true,
      },
    },
    {
      breakpoint: 568,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        dots: false,
        arrows: false,
      },
    },
  ],
});
//newest
$(".slider-newest").slick({
  nextArrow: ".next-arrow-newest",
  prevArrow: ".prev-arrow-newest",
  dots: false,
  slidesToShow: 4,
  slidesToScroll: 1,
  rtl: true,
  arrows: true,
  responsive: [
    {
      breakpoint: 1920,
      settings: {
        slidesToShow: 4,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
        arrows: true,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        dots: false,
        arrows: true,
      },
    },
    {
      breakpoint: 568,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        arrows: false,
      },
    },
  ],
});
//newest phone
$(".slider-phones").slick({
  nextArrow: ".next-arrow-phones",
  prevArrow: ".prev-arrow-phones",
  dots: false,
  slidesToShow: 4,
  slidesToScroll: 1,
  rtl: true,
  arrows: true,
  responsive: [
    {
      breakpoint: 1920,
      settings: {
        slidesToShow: 4,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
        arrows: true,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        dots: false,
        arrows: true,
      },
    },
    {
      breakpoint: 568,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        arrows: false,
      },
    },
  ],
});
//newest phone
$(".slider-watches").slick({
  nextArrow: ".next-arrow-watches",
  prevArrow: ".prev-arrow-watches",
  dots: false,
  slidesToShow: 4,
  slidesToScroll: 1,
  rtl: true,
  arrows: true,
  responsive: [
    {
      breakpoint: 1920,
      settings: {
        slidesToShow: 4,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
        arrows: true,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        dots: false,
        arrows: true,
      },
    },
    {
      breakpoint: 568,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        arrows: false,
      },
    },
  ],
});
//slider-recently-blog
$(".slider-recent-blog").slick({
  dots: true,
  slidesToShow: 1,
  slidesToScroll: 1,
  rtl: true,
  arrows: false,
});
