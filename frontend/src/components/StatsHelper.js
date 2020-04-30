import React from "react";
import StatsCountry from "../layouts/StatsCountry";

const statsHelper = (props) => {
    return (
        <StatsCountry country={props.match.params.country}/>
    )
};

export default statsHelper;