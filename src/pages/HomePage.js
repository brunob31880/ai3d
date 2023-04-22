// HomePage.js
import React from 'react';
import AscViewer from '../components/ReliefViewer';

function HomePage() {
    return (
        <div>
            <AscViewer shapefileUrl="../datas/ASC/testasc.asc" />
        </div>
    );
}

export default HomePage;