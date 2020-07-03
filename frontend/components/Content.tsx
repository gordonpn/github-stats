import { Flex, Text } from "@chakra-ui/core";
import React, { ReactElement } from "react";
import { Doughnut, Bar } from "react-chartjs-2";
import GitHubCalendar from "react-github-calendar";
import ReactTooltip from "react-tooltip";

const doughnutData = {
  labels: ["Red", "Green", "Yellow"],
  datasets: [
    {
      data: [300, 50, 100],
      backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
      hoverBackgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
    },
  ],
};

const barData = {
  labels: ["January", "February", "March", "April", "May", "June", "July"],
  datasets: [
    {
      label: "Commits",
      backgroundColor: "rgba(131,115,222,0.2)",
      borderColor: "rgba(131,115,222,1)",
      borderWidth: 1,
      hoverBackgroundColor: "rgba(131,115,222,0.4)",
      hoverBorderColor: "rgba(131,115,222,1)",
      data: [65, 59, 80, 81, 56, 55, 40],
    },
  ],
};

export default function Content(): ReactElement {
  return (
    <>
      <Flex flexDirection="column" width="60vw">
        <Text>Here&apos;s my current contribution calendar on GitHub.</Text>
        <Text>As you can see, I like working on software development!</Text>
      </Flex>
      <Flex flexDirection="column" margin="5vh">
        <GitHubCalendar
          username="gordonpn"
          color="hsl(249, 62%, 66%)"
          blockSize={15}
          blockMargin={1}
          showTotalCount={false}
        >
          <ReactTooltip delayShow={50} html />
        </GitHubCalendar>
      </Flex>
      <Flex flexDirection="column" width="60vw">
        <Text>Which languages do I like?</Text>
        <Text>Here is a breakdown of languages I tend to use!</Text>
      </Flex>
      <Flex flexDirection="column" margin="5vh">
        <Doughnut height={350} width={350} data={doughnutData} />
      </Flex>
      <Flex flexDirection="column" width="60vw">
        <Text>When do I make commits?</Text>
        <Text>
          I was curious about my own working habits, so here is a breakdown of
          what time of the day I tend to commit and which day of the week I tend
          to make commits.
        </Text>
      </Flex>
      <Flex
        justifyContent="space-around"
        alignItems="center"
        flexDirection={["column", "row"]}
        width={["90vw", "40vw"]}
        height={["50vh", "25vh"]}
        margin="10vh"
      >
        <Bar data={barData} />
        <Bar data={barData} />
      </Flex>
    </>
  );
}
