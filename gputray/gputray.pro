CUDASDK = "D:/NVIDIA/NVIDIA GPU Computing Toolkit/CUDA/v10.1/"

INCLUDEPATH += $$CUDASDK/include
HEADERS       = window.h
SOURCES       = main.cpp \
                window.cpp
RESOURCES     = gputray.qrc
CONFIG += static
QT += widgets
requires(qtConfig(combobox))

LIBS += -L"$$CUDASDK/lib/x64"
LIBS += -lnvml


# install
target.path = C:\Users\Francois\src\qt\gputray_bin
INSTALLS += target
