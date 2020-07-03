import { Flex, Text } from "@chakra-ui/core";
import { Pie } from "react-chartjs-2";
import React, { ReactElement, useEffect, useState } from "react";
import axios from "axios";

export default function Languages(): ReactElement {
  const [loaded, setLoaded] = useState(false);
  const [state, setState] = useState({
    labels: [],
    datasets: [
      {
        data: [],
        // TODO generate tints and shades programmatically
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
  });

  useEffect(() => {
    const fetchData = async () => {
      await axios.get("/api/v1/languages").then((response) => {
        const data = response.data;
        const labels = [];
        const chartData = [];
        Object.entries(data).forEach(([key, value]) => {
          labels.push(key);
          chartData.push(value);
        });
        const updatedState = { ...state };
        updatedState.labels = [...labels];
        updatedState.datasets[0].data = [...chartData];
        setState(updatedState);
      });
    };
    fetchData().then(() => {
      setLoaded(true);
    });
  }, []);

  return (
    <>
      <Flex flexDirection="column" width="60vw">
        <Text>Which languages do I like?</Text>
        <Text>
          Here is a breakdown of languages I tend to use in percentages (%).
        </Text>
      </Flex>
      <Flex flexDirection="column" margin="5vh">
        <Pie height={350} width={350} data={state} />
      </Flex>
    </>
  );
}
