import { Flex, Text } from "@chakra-ui/core";
import React, { ReactElement } from "react";
import GitHubCalendar from "react-github-calendar";
import ReactTooltip from "react-tooltip";
import LanguagesCharts from "@/components/LanguagesCharts";
import Commits from "@/components/Commits";

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
      <LanguagesCharts />
      <Commits />
    </>
  );
}
