import { Container } from "@/components/Container";
import { Hero } from "@/components/Hero";
import React, { ReactElement } from "react";
import Content from "@/components/Content";

export default function Index(): ReactElement {
  return (
    <Container>
      <Hero title={"GitHub Stats"} />
      <Content />
    </Container>
  );
}
