import {
  makeStyles,
  Body1,
  Button,
  CardFooter,
  Field,
  Textarea,
  Spinner,
} from "@fluentui/react-components";
import { useEffect, useRef, useState } from "react";
import { Delete24Regular, SendRegular } from "@fluentui/react-icons";
import { Message } from "./Message";
import { Response } from "./Response";
import { useEventDataContext } from "../../providers/EventDataProvider";
import type { ChatMessage } from "@azure/openai";
import { Card } from "./Card";

interface CardProps {
  onPromptEntered: (messages: ChatMessage[]) => void;
  messageList: ChatMessage[];
  onClear: () => void;
  isLoading: boolean;
}

const useStyles = makeStyles({
  card: {
    display: "flex",
    height: "calc(100vh - 70px)",
  },
  dialog: {
    display: "block",
  },
  smallButton: {
    width: "100%",
    height: "50%",
    maxWidth: "none",
  },
  startCard: {
    display: "flex",
    maxWidth: "80%",
    marginTop: "35%",
    marginLeft: "20%",
    marginRight: "20%",
    marginBottom: "35%",
  },
});

export const ChatCard = ({
  onPromptEntered,
  messageList,
  onClear,
  isLoading,
}: CardProps) => {
  const chat = useStyles();
  const chatContainerRef = useRef<HTMLDivElement>(null);
  const { isAuthorized } = useEventDataContext();

  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop =
        chatContainerRef.current.scrollHeight;
    }
  }, [messageList]);

  return (
    <Card className={chat.card} header="Chat Session">
      <div
        id={"chatContainer"}
        style={{ overflowY: "auto" }}
        ref={chatContainerRef}
      >
        {messageList.length > 1 ? (
          messageList.map((message, index) => {
            if (message.role === "system") {
              return null;
            }
            return message.role === "user" ? (
              <Message key={index} message={message} />
            ) : (
              <Response key={index} message={message} />
            );
          })
        ) : (
          <Card className={chat.startCard}>
            <Body1 style={{ textAlign: "center" }}>
              <h2>Start Chatting</h2>
            </Body1>
          </Card>
        )}
      </div>
      {isLoading && <Spinner />}
      {isAuthorized && (
        <ChatInput
          promptSubmitted={(userPrompt) => {
            onPromptEntered([
              ...messageList,
              { role: "user", content: userPrompt },
            ]);
          }}
          onClear={onClear}
        />
      )}
      {!isAuthorized && (
        <>
          <CardFooter style={{ height: "10vh" }}>
            <p>Please enter your event code to start the chat session.</p>
          </CardFooter>
        </>
      )}
    </Card>
  );
};

function ChatInput({
  promptSubmitted,
  onClear,
}: {
  promptSubmitted: (userPrompt: string) => void;
  onClear: () => void;
}) {
  const [userPrompt, setPrompt] = useState("");

  const chat = useStyles();
  return (
    <CardFooter style={{ height: "10vh" }}>
      <Field className="user-query" style={{ width: "100%" }}>
        <Textarea
          style={{}}
          value={userPrompt}
          placeholder="Type user query here (Shift + Enter for new line)"
          onChange={(event) => {
            setPrompt(event.target.value);
          }}
          onKeyDown={(event) => {
            if (event.key === "Enter" && !event.shiftKey) {
              promptSubmitted(userPrompt);
              setPrompt("");
              event.preventDefault();
            }
          }}
        />
      </Field>
      <div>
        <Button
          className={chat.smallButton}
          id={"send-button"}
          icon={<SendRegular />}
          iconPosition="after"
          onClick={() => {
            promptSubmitted(userPrompt);
            setPrompt("");
          }}
        >
          Send
        </Button>
        <Button
          className={chat.smallButton}
          id="clear-button"
          icon={<Delete24Regular />}
          iconPosition="after"
          onClick={onClear}
        >
          Clear Chat
        </Button>
      </div>
    </CardFooter>
  );
}
