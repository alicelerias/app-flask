export type Response = {
  field_name: string;
  value: string | number;
};

export type Responses = ResultList<"responses", Response>;

export type ProposalField = {
  name: string;
  type: any;
  nullable: boolean;
  order: number;
};

export type ProposalFields = ProposalField[];

export type ResultList<K extends string, T> = {
  [P in K]: T[];
};
