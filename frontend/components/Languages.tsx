import { Flex, Text } from "@chakra-ui/core";
import { Pie } from "react-chartjs-2";
import React, { ReactElement } from "react";

const data = {
  labels: [
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
  ],
  datasets: [
    {
      data: [
        1.33,
        1.74,
        0.79,
        1.72,
        6.73,
        3.02,
        29.1,
        27.0,
        0.44,
        2.5,
        8.26,
        3.95,
        10.3,
        2.04,
        0.88,
      ],
      backgroundColor: [
        "#8373de",
        "#8f81e1",
        "#9b8fe4",
        "#a89de7",
        "#b4abeb",
        "#c1b9ee",
        "#cdc7f1",
        "#d9d5f5",
        "#e6e3f8",
        "#7567c7",
        "#685cb1",
        "#5b509b",
        "#4e4585",
        "#41396f",
        "#342e58",
      ],
      hoverBackgroundColor: [
        "#8373de",
        "#8f81e1",
        "#9b8fe4",
        "#a89de7",
        "#b4abeb",
        "#c1b9ee",
        "#cdc7f1",
        "#d9d5f5",
        "#e6e3f8",
        "#7567c7",
        "#685cb1",
        "#5b509b",
        "#4e4585",
        "#41396f",
        "#342e58",
      ],
    },
  ],
};

export default function Languages(): ReactElement {
  return (
    <>
      <Flex flexDirection="column" width="60vw">
        <Text>Which languages do I like?</Text>
        <Text>
          Here is a breakdown of languages I tend to use in percentages (%).
        </Text>
      </Flex>
      <Flex flexDirection="column" margin="5vh">
        <Pie height={350} width={350} data={data} />
      </Flex>
    </>
  );
}
