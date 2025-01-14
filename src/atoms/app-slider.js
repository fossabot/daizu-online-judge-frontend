import React from "react";
import Slider from "react-slick";
import Button from "./app-button-normal";
import Card from "../pages/temp/test-card";

class SimpleSlider extends React.Component {
  render() {
    var settings = {
      dots: true,
      infinite: true,
      speed: 500,
      slidesToShow: 1,
      slidesToScroll: 1,
      autoplay: true,
    };

    return (
      <Slider {...settings}>
        <div>
          <h3>1</h3>
          <Button buttonText="はろーわーるど！" />
        </div>
        <div>
          <Card />
        </div>
        <div>
          <h3>3</h3>
        </div>
        <div>
          <h3>4</h3>
        </div>
        <div>
          <h3>5</h3>
        </div>
      </Slider>
    );
  }
}

export default SimpleSlider;
