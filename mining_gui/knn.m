function varargout = knn(varargin)
% KNN MATLAB code for knn.fig
%      KNN, by itself, creates a new KNN or raises the existing
%      singleton*.
%
%      H = KNN returns the handle to a new KNN or the handle to
%      the existing singleton*.
%
%      KNN('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in KNN.M with the given input arguments.
%
%      KNN('Property','Value',...) creates a new KNN or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before knn_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to knn_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help knn

% Last Modified by GUIDE v2.5 21-Apr-2021 17:35:51

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @knn_OpeningFcn, ...
                   'gui_OutputFcn',  @knn_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before knn is made visible.
function knn_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to knn (see VARARGIN)

% Choose default command line output for knn
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes knn wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = knn_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in btn_show.
function btn_show_Callback(hObject, eventdata, handles)
% hObject    handle to btn_show (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
opts = detectImportOptions('ecoli.csv');
opts.SelectedVariableNames = (2:8);
data = readmatrix('ecoli.csv',opts);
set(handles.table1,'data',data);


function mcg_Callback(hObject, eventdata, handles)
% hObject    handle to mcg (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of mcg as text
%        str2double(get(hObject,'String')) returns contents of mcg as a double


% --- Executes during object creation, after setting all properties.
function mcg_CreateFcn(hObject, eventdata, handles)
% hObject    handle to mcg (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function gvh_Callback(hObject, eventdata, handles)
% hObject    handle to gvh (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of gvh as text
%        str2double(get(hObject,'String')) returns contents of gvh as a double


% --- Executes during object creation, after setting all properties.
function gvh_CreateFcn(hObject, eventdata, handles)
% hObject    handle to gvh (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function lip_Callback(hObject, eventdata, handles)
% hObject    handle to lip (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of lip as text
%        str2double(get(hObject,'String')) returns contents of lip as a double


% --- Executes during object creation, after setting all properties.
function lip_CreateFcn(hObject, eventdata, handles)
% hObject    handle to lip (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function chg_Callback(hObject, eventdata, handles)
% hObject    handle to chg (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of chg as text
%        str2double(get(hObject,'String')) returns contents of chg as a double


% --- Executes during object creation, after setting all properties.
function chg_CreateFcn(hObject, eventdata, handles)
% hObject    handle to chg (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function aac_Callback(hObject, eventdata, handles)
% hObject    handle to aac (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of aac as text
%        str2double(get(hObject,'String')) returns contents of aac as a double


% --- Executes during object creation, after setting all properties.
function aac_CreateFcn(hObject, eventdata, handles)
% hObject    handle to aac (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function alm1_Callback(hObject, eventdata, handles)
% hObject    handle to alm1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of alm1 as text
%        str2double(get(hObject,'String')) returns contents of alm1 as a double


% --- Executes during object creation, after setting all properties.
function alm1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to alm1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function alm2_Callback(hObject, eventdata, handles)
% hObject    handle to alm2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of alm2 as text
%        str2double(get(hObject,'String')) returns contents of alm2 as a double


% --- Executes during object creation, after setting all properties.
function alm2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to alm2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in btn_class.
function btn_class_Callback(hObject, eventdata, handles)
% hObject    handle to btn_class (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

mcg = str2double(get(handles.mcg,'String'));
gvh = str2double(get(handles.gvh,'String'));
lip = str2double(get(handles.lip,'String'));
chg = str2double(get(handles.chg,'String'));
aac = str2double(get(handles.aac,'String'));
alm1 = str2double(get(handles.alm1,'String'));
alm2 = str2double(get(handles.alm2,'String'));

sample = [mcg gvh lip chg aac alm1 alm2];

opts = detectImportOptions('ecoli.csv');
opts.SelectedVariableNames = (2:8);
training = readmatrix('ecoli.csv',opts);

opts = detectImportOptions('ecoli.csv');
opts.SelectedVariableNames = (1);
group = readmatrix('ecoli.csv',opts);

class = fitcknn(training, group, 'NumNeighbor', 3);
klasifikasi = predict(class, sample);

set(handles.hasil, 'string', klasifikasi);


% --- Executes on button press in btn_reset.
function btn_reset_Callback(hObject, eventdata, handles)
% hObject    handle to btn_reset (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(handles.mcg, 'string', []);
set(handles.gvh, 'string', []);
set(handles.lip, 'string', []);
set(handles.chg, 'string', []);
set(handles.aac, 'string', []);
set(handles.alm1, 'string', []);
set(handles.alm2, 'string', []);
set(handles.hasil, 'string', []);
clear;

% --- Executes on button press in btn_clear.
function btn_clear_Callback(hObject, eventdata, handles)
% hObject    handle to btn_clear (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
data = [];
set(handles.table1,'data',data);
clear;
