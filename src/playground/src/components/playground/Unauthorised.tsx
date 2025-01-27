import {
  Button,
  Dialog,
  DialogActions,
  DialogBody,
  DialogContent,
  DialogSurface,
  DialogTitle,
  DialogTrigger,
} from "@fluentui/react-components";
import {
  AuthStatus,
  useEventDataContext,
} from "../../providers/EventDataProvider";

export const Unauthorised = () => {
  const { authStatus, setEventCode: setEventConnection } =
    useEventDataContext();

  if (authStatus !== AuthStatus.NotAuthorized) {
    return null;
  }

  return (
    <Dialog open={true}>
      <DialogSurface>
        <DialogBody>
          <DialogTitle>Invalid Event Code</DialogTitle>
          <DialogContent>
            The event code provided is invalid, please check the code and try
            again.
          </DialogContent>
          <DialogActions>
            <DialogTrigger disableButtonEnhancement>
              <Button
                appearance="primary"
                onClick={() => setEventConnection("")}
              >
                Close
              </Button>
            </DialogTrigger>
          </DialogActions>
        </DialogBody>
      </DialogSurface>
    </Dialog>
  );
};
