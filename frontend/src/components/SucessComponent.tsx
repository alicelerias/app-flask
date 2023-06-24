import React from "react";

type props = {
  message: string;
};

export const SucessComponent: React.FC<props> = ({ message }) => {
  return <p className="text-green-600">{message}</p>;
};
