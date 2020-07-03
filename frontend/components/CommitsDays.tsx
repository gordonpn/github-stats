import { Bar } from "react-chartjs-2";
import React, { ReactElement, useEffect, useState } from "react";
import axios from "axios";

// TODO combine hours and days into same component

export default function CommitsDays(): ReactElement {
  const [loaded, setLoaded] = useState(false);
  const [state, setState] = useState({
    labels: [],
    datasets: [
      {
        label: "Commits per weekday",
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
      await axios.get("/api/v1/commits/days").then((response) => {
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
      <Bar data={state} />
    </>
  );
}
