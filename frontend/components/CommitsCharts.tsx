import { Bar } from "react-chartjs-2";
import React, { ReactElement, useEffect, useState } from "react";
import axios from "axios";
import PropTypes from "prop-types";
import Skeleton from "react-loading-skeleton";

interface Props {
  type: string;
}

interface IState {
  labels: string[];
  datasets: IDataset[];
}

interface IDataset {
  label: string;
  data: number[];
  backgroundColor: string;
  hoverBackgroundColor: string;
  borderColor: string;
  hoverBorderColor: string;
}

CommitsCharts.propTypes = {
  type: PropTypes.oneOf(["days", "hours"]).isRequired,
};

export default function CommitsCharts(props: Props): ReactElement {
  const { type } = props;
  const [loaded, setLoaded] = useState(false);
  const [state, setState] = useState({
    labels: [],
    datasets: [
      {
        label: "",
        backgroundColor: "rgba(131,115,222,0.2)",
        hoverBackgroundColor: "rgba(131,115,222,0.4)",
        borderColor: "rgba(131,115,222,1)",
        borderWidth: 1,
        hoverBorderColor: "rgba(131,115,222,1)",
        data: [],
      },
    ],
  });

  useEffect(() => {
    const fetchData = async () => {
      await axios.get(`/api/v1/commits/${type}`).then((response) => {
        const data = response.data;
        const labels: string[] = [];
        const chartData: number[] = [];
        Object.entries(data).forEach(([key, value]) => {
          if (typeof value === "number") {
            labels.push(key);
            chartData.push(value);
          }
        });
        const updatedState: IState = { ...state };
        updatedState.datasets[0].label = `Commits per ${type.slice(0, -1)}`;
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

  return (
    <>
      {loaded ? <Bar data={state} /> : <Skeleton height="25vh" width="40vw" />}
    </>
  );
}
