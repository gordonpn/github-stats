import { Flex } from "@chakra-ui/core";
import React, { ReactElement } from "react";
import { Doughnut } from "react-chartjs-2";

const data = {
  labels: ["Red", "Green", "Yellow"],
  datasets: [
    {
      data: [300, 50, 100],
      backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
      hoverBackgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
    },
  ],
};

export default function Content(): ReactElement {
  return (
    <Flex direction="row">
      <Doughnut width={350} height={350} data={data} />
    </Flex>
  );
}
