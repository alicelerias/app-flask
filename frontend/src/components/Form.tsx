import { useState } from "react";

import { FieldValues, useForm } from "react-hook-form";
import { useQuery, useMutation } from "react-query";

import { getForm } from "../api/queries";
import { createResponse } from "../api/mutations";
import { Responses } from "../types";
import { SucessComponent } from "./SucessComponent";

export const Form = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm();
  const [sucess, showSucess] = useState(false);
  const onSubmit = (data: FieldValues) => {
    const entries = Object.entries(data);
    const responses: Responses = {
      responses: entries.map(([field_name, value]) => ({ field_name, value })),
    };
    mutate(responses);
  };

  const { data, isLoading } = useQuery("getForm", () => getForm());
  const { mutate } =
    useMutation(createResponse, {
      onSuccess: () => {
        showSucess(true);
        setTimeout(() => {
          showSucess(false);
          reset();
        }, 2000);
      },
    }) || {};

  return (
    <div className="flex gap-2 items-center justify-center h-screen">
      <div className="flex flex-col min-w-[50vw] gap-2 bg-gray-300 p-4 rounded-lg shadow-md">
        {sucess ? (
          <SucessComponent message="Proposta enviada com sucesso" />
        ) : (
          <>
            <h1 className="text-2xl text-center text-green-600 font-bold mb-2">
              Envie-nos uma proposta
            </h1>

            <form
              className="flex flex-col gap-2"
              onSubmit={handleSubmit(onSubmit)}
            >
              {data ? (
                data.length > 0 ? (
                  data.map((field) => (
                    <div className="flex flex-col" key={field.name}>
                      <input
                        className="p-2"
                        {...register(field.name, {
                          required: field.nullable ? false : true,
                        })}
                        type={field.type === "integer" ? "number" : "text"}
                        placeholder={field.name}
                        onClick={() => console.log(field.nullable)}
                      />
                      {errors[field.name] && (
                        <div className="flex justify-center text-red-600 text-sm p-1">
                          {(errors[field.name]?.message as string) ||
                            "Campo inválido"}{" "}
                        </div>
                      )}
                    </div>
                  ))
                ) : (
                  <p className="flex justify-center text-green-600">
                    Ainda não temos campos para preencher, volte mais tarde.
                  </p>
                )
              ) : (
                <div className="animate-pulse bg-gray-400 h-10 rounded"></div>
              )}

              {data && data.length > 0 && (
                <button
                  type="submit"
                  disabled={isLoading}
                  className="bg-green-500 mt-3 mx-auto w-auto hover:bg-green-600 text-gray-200 font-bold py-2 px-4 shadow-md"
                >
                  Enviar
                </button>
              )}
            </form>
          </>
        )}
      </div>
    </div>
  );
};
