import { Bar } from "react-chartjs-2";
import React, { ReactElement } from "react";

const barData = {
  labels: [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ],
  datasets: [
    {
      label: "Commits per hour",
      backgroundColor: "rgba(131,115,222,0.2)",
      hoverBackgroundColor: "rgba(131,115,222,0.4)",
      borderColor: "rgba(131,115,222,1)",
      borderWidth: 1,
      hoverBorderColor: "rgba(131,115,222,1)",
      data: [102, 181, 147, 221, 146, 175, 205],
    },
  ],
};

export default function CommitsHours(): ReactElement {
  return (
    <>
      <Bar data={barData} />
    </>
  );
}
