import { Container } from "@/components/Container";
import React, { ReactElement } from "react";
import Content from "@/components/Content";
import Hero from "@/components/Hero";
import Footer from "@/components/Footer";

export default function Index(): ReactElement {
  return (
    <Container>
      <Hero title={"GitHub Stats"} />
      <Content />
      <Footer />
    </Container>
  );
}
