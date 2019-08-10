import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import PropTypes from "prop-types";

const useStyles = makeStyles(theme => ({
  root: {
    margin: "auto",
    textAlign: "center",
    justifyContent: "center",
    fontFamily: ["Noto Sans JS", "sans-serif"].join(","),
  },
  card: {
    minWidth: 275,
    padding: theme.spacing(3),
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.secondary.contrastText,
  },
  title: {
    fontWeight: "bolder",
    margin: theme.spacing(1),
  },
  subtitle: {
    marginBottom: theme.spacing(2),
  },
  button: {
    margin: theme.spacing(1),
    paddingLeft: theme.spacing(3),
    paddingRight: theme.spacing(3),
  },
}));

SliderItem.propTypes = {
  contestTitle: PropTypes.string,
  contestDate: PropTypes.string,
  contestTime: PropTypes.string,
  contestContent: PropTypes.string,
};
export default function SliderItem(props) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Card className={classes.card} elevation={0}>
        <CardContent>
          <Typography variant="h3" className={classes.title}>
            {props.contestTitle}
          </Typography>
          <Typography variant="subtitle1" className={classes.subtitle}>
            {props.contestDate} {props.contestTime}
          </Typography>
          <Typography variant="body1">{props.contestContent}</Typography>
        </CardContent>
        <CardActions classes={{ root: classes.root }}>
          <Button size="small" color="secondary" variant="contained" className={classes.button}>
            参加する
          </Button>
        </CardActions>
      </Card>
    </div>
  );
}