import { Flex, Text } from "@chakra-ui/core";
import { Pie } from "react-chartjs-2";
import React, { ReactElement, useEffect, useState } from "react";
import axios from "axios";
// @ts-ignore
import Values from "values.js";
import Skeleton from "react-loading-skeleton";
import useWindowSize from "../src/useWindowSize";

interface IState {
  labels: string[];
  datasets: IDataset[];
}

interface IDataset {
  data: number[];
  backgroundColor: string[];
  hoverBackgroundColor: string[];
}

const round = (value: number, precision: number) => {
  const multiplier = Math.pow(10, precision || 0);
  return Math.round(value * multiplier) / multiplier;
};

export default function LanguagesCharts(): ReactElement {
  const [loaded, setLoaded] = useState(false);
  const size = useWindowSize();
  const [state, setState] = useState({
    labels: [],
    datasets: [
      {
        data: [],
        backgroundColor: [],
        hoverBackgroundColor: [],
      },
    ],
  });

  useEffect(() => {
    const fetchData = async () => {
      await axios.get("/api/v1/languages").then((response) => {
        const data = response.data;
        const labels: string[] = [];
        const chartData: number[] = [];
        Object.entries(data).forEach(([key, value]) => {
          if (typeof value === "number") {
            labels.push(key);
            chartData.push(round(value, 1));
          }
        });
        const updatedState: IState = { ...state };
        updatedState.labels = [...labels];
        updatedState.datasets[0].data = [...chartData];
        // @ts-ignore
        setState(updatedState);
      });
    };
    fetchData().then(() => {
      setLoaded(true);
    });
  }, []);

  useEffect(() => {
    const colour = new Values("#8373de");
    const values = colour.all(10);
    const colours: string[] = [];
    values.forEach((value: { hexString: () => any }) => {
      if (value.hexString() !== "#ffffff") {
        colours.push(value.hexString());
      }
    });
    const updatedState: IState = { ...state };
    updatedState.datasets[0].backgroundColor = [...colours];
    updatedState.datasets[0].hoverBackgroundColor = [...colours];
    // @ts-ignore
    setState(updatedState);
  }, []);

  const getSize = (): number => {
    if (size.width === undefined) {
      return 350;
    }
    const chartSize = ~~(size.width * 0.45);
    if (chartSize <= 500) {
      return size.width;
    }
    return chartSize;
  };

  return (
    <>
      <Flex flexDirection="column" width="60vw">
        <Text fontSize="xl">Which languages do I like?</Text>
        <Text>
          Here is a breakdown of languages I tend to use in percentages (%).
        </Text>
        <Text>
          Including both <Text as="u"> private and public</Text> repositories.
        </Text>
      </Flex>
      <Flex flexDirection="column" margin="5vh">
        {loaded ? (
          <Pie height={getSize()} width={getSize()} data={state} />
        ) : (
          <Skeleton circle={true} height={getSize()} width={getSize()} />
        )}
      </Flex>
    </>
  );
}
