var multipleCardCarousel = document.querySelector(
  "#carouselExampleControls"
);

  if (window.matchMedia("(min-width: 768px)").matches && window.matchMedia("(max-width: 992px)").matches) {
    console.log("MD: Min-width: 768px, Max-width: 992px")
    var carousel = new bootstrap.Carousel(multipleCardCarousel, {
      interval: false,
    });
    var carouselWidth = $(".carousel-inner")[0].scrollWidth;
    var cardWidth = $(".carousel-item").width();
    var marginCard = parseInt( $(".carousel-item").css("marginRight") );
    var scrollPosition = 0;
    $("#carouselExampleControls .carousel-control-next").on("click", function () {
      if (scrollPosition < carouselWidth - cardWidth * 3) {
        console.log("Before:" + scrollPosition)
        scrollPosition += cardWidth + marginCard;
        console.log("cardWidth: " + cardWidth)
        console.log("marginCard: " + marginCard)
        console.log(scrollPosition)
        $("#carouselExampleControls .carousel-inner").animate(
          { scrollLeft: scrollPosition },
          600
        );
      }
    });
    $("#carouselExampleControls .carousel-control-prev").on("click", function () {
      if (scrollPosition > 0) {
        console.log("Before:" + scrollPosition)
        scrollPosition = scrollPosition - cardWidth - marginCard;
        console.log("cardWidth: " + cardWidth)
        console.log("marginCard: " + marginCard)
        console.log(scrollPosition)
        $("#carouselExampleControls .carousel-inner").animate(
          { scrollLeft: scrollPosition },
          600
        );
      }
    });
  }
  else if (window.matchMedia("(min-width: 992px)").matches && window.matchMedia("(max-width: 1200px)").matches) {
    console.log("LG: Min-width: 992px, Max-width: 1200px")
    var carousel = new bootstrap.Carousel(multipleCardCarousel, {
      interval: false,
    });
    var carouselWidth = $(".carousel-inner")[0].scrollWidth;
    var cardWidth = $(".carousel-item").width();
    var marginCard = parseInt( $(".carousel-item").css("marginRight") );
    var scrollPosition = 0;
    $("#carouselExampleControls .carousel-control-next").on("click", function () {
      if (scrollPosition < carouselWidth - cardWidth * 3) {
        console.log("Before:" + scrollPosition)
        scrollPosition += cardWidth + marginCard;
        console.log("cardWidth: " + cardWidth)
        console.log("marginCard: " + marginCard)
        console.log(scrollPosition)
        $("#carouselExampleControls .carousel-inner").animate(
          { scrollLeft: scrollPosition },
          600
        );
      }
    });
    $("#carouselExampleControls .carousel-control-prev").on("click", function () {
      if (scrollPosition > 0) {
        console.log("Before:" + scrollPosition)
        scrollPosition = scrollPosition - cardWidth - marginCard;
        console.log("cardWidth: " + cardWidth)
        console.log("marginCard: " + marginCard)
        $("#carouselExampleControls .carousel-inner").animate(
          { scrollLeft: scrollPosition },
          600
        );
      }
    });
  }
  else if (window.matchMedia("(min-width: 1200px)").matches) {
    console.log("XL (and following): Min-width: 1200px")
    var carousel = new bootstrap.Carousel(multipleCardCarousel, {
      interval: false,
    });
    var carouselWidth = $(".carousel-inner")[0].scrollWidth;
    var cardWidth = $(".carousel-item").width();
    var marginCard = parseInt( $(".carousel-item").css("marginRight") );
    var scrollPosition = 0;
    $("#carouselExampleControls .carousel-control-next").on("click", function () {
      if (scrollPosition < carouselWidth - cardWidth * 4) {
        console.log("Before:" + scrollPosition)
        scrollPosition += cardWidth + marginCard;
        console.log("cardWidth: " + cardWidth)
        console.log("marginCard: " + marginCard)
        console.log(scrollPosition)
        $("#carouselExampleControls .carousel-inner").animate(
          { scrollLeft: scrollPosition },
          600
        );
      }
    });
    $("#carouselExampleControls .carousel-control-prev").on("click", function () {
      if (scrollPosition > 0) {
        console.log("Before:" + scrollPosition)
        scrollPosition = scrollPosition - cardWidth - marginCard;
        console.log("cardWidth: " + cardWidth)
        console.log("marginCard: " + marginCard)
        console.log(scrollPosition)
        $("#carouselExampleControls .carousel-inner").animate(
          { scrollLeft: scrollPosition },
          600
        );
      }
    });
  }
  else {
    $(multipleCardCarousel).removeClass("slide");
  }