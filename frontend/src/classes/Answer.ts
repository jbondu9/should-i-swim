import { ApiAnswer } from "../interfaces/ApiAnswer";

export class Answer {
  status: string;
  description: string;

  constructor(answer?: ApiAnswer) {
    this.status = answer?.status ?? "";
    this.description = answer?.description ?? "";
  }
}
