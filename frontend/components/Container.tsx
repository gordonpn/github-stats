import { Flex } from "@chakra-ui/core";
import React, { ReactElement } from "react";

interface Props {}

export const Container = (props: Props): ReactElement => {
  return (
    <Flex
      direction="column"
      alignItems="center"
      justifyContent="flex-start"
      {...props}
    />
  );
};
